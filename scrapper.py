import os 
# 1. Import JsonConfig from the library
from firecrawl import AsyncFirecrawlApp, JsonConfig
import json
from dotenv import load_dotenv
import asyncio
import pandas as pd
from datetime import datetime
# Assuming 'Car' model is defined as before
from models import Car

load_dotenv()
app = AsyncFirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

async def extract_cars(url: str, schema: dict, prompt: str):
    """Extracts car data using the correct formats and json_options parameters."""
    try:
        json_cfg = JsonConfig(schema=schema, prompt=prompt)

        # THE FIX IS HERE: Add formats=['json'] alongside json_options
        response = await asyncio.wait_for(
            app.scrape_url(
                url,
                formats=['json'], 
                json_options=json_cfg
            ),
            timeout=600
        )
        
        # The rest of your function remains the same
        if response and response.json:
            extracted_data = response.json
            
            items = extracted_data.get('variants', []) if 'variants' in extracted_data else [extracted_data]

            props = []
            for obj in items:
                if isinstance(obj, dict):
                    props.append(Car(
                        manufacturer=obj.get("manufacturer", ""),
                        model_name=obj.get("model_name", ""),
                        manufacturing_year=obj.get("manufacturing_year", "2025"),
                        variant_name=obj.get("variant_name", ""),
                        showroom_price=obj.get("showroom_price", ""),
                        fuel_type=obj.get("fuel_type", ""),
                        engine_capacity_cc=str(obj.get("engine_capacity_cc", "")),
                        body_type=obj.get("body_type", ""),
                        seating_capacity=str(obj.get("seating_capacity", "")),
                        torque_nm=obj.get("torque_nm", ""),
                        mileage_kmpl=obj.get("mileage_kmpl", ""),
                        power_bhp=obj.get("power_bhp", ""),
                        transmission=obj.get("transmission", ""),
                        safety_rating=obj.get("safety_rating", ""),
                        features=obj.get("features", []),
                    ))
            
            print(f"✅ Extracted {len(props)} car variants from {url}")
            return props
        else:
            print(f"⚠️ No '.json' data found in the response object from {url}")
            return []

    except asyncio.TimeoutError:
        print(f"❌ Timeout occurred while scraping {url} after 180 seconds.")
        return []
    except Exception as e:
        print(f"❌ Error scraping {url}: {str(e)}")
        return []

def convert_to_csv(car_details, filename=None):
    """Convert car data to pandas DataFrame and export as CSV"""
    if not car_details:
        print("❌ No car data to convert")
        return None
    
    # Convert Car objects to dictionaries
    car_dicts = []
    for car in car_details:
        car_dict = car.__dict__.copy()
        # Convert features list to comma-separated string
        if isinstance(car_dict.get('features'), list):
            car_dict['features'] = ', '.join(car_dict['features'])
        car_dicts.append(car_dict)
    
    # Create DataFrame
    df = pd.DataFrame(car_dicts)
    
    # Reorder columns for better readability
    column_order = [
        'manufacturer',
        'model_name', 
        'variant_name',
        'manufacturing_year',
        'showroom_price',
        'fuel_type',
        'engine_capacity_cc',
        'body_type',
        'seating_capacity',
        'transmission',
        'power_bhp',
        'torque_nm',
        'mileage_kmpl',
        'safety_rating',
        'features'
    ]
    
    # Reorder columns (only include columns that exist)
    existing_columns = [col for col in column_order if col in df.columns]
    df = df[existing_columns]
    
    # Generate filename if not provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"car_data_{timestamp}.csv"
    
    # Export to CSV
    df.to_csv(filename, index=False, encoding='utf-8')
    
    print(f"✅ Successfully exported {len(df)} cars to {filename}")
    print(f"📊 Columns: {', '.join(df.columns.tolist())}")
    print(f"📈 Data shape: {df.shape}")
    
    # Display first few rows as preview
    print("\n📋 Preview of exported data:")
    print(df.head().to_string())
    
    return df

async def fetch_vehicle_data():
    test_urls = [
        "https://www.cardekho.com/cars/Tesla",
        "https://www.cardekho.com/cars/Pravaig",
        "https://www.cardekho.com/cars/Rolls-Royce",
        "https://www.cardekho.com/cars/BYD",
        "https://www.cardekho.com/cars/Jaguar",
        "https://www.cardekho.com/cars/Lotus",
        "https://www.cardekho.com/cars/Isuzu",
        "https://www.cardekho.com/cars/Lexus",
        "https://www.cardekho.com/cars/Ferrari",
        "https://www.cardekho.com/cars/Land_Rover",
        "https://www.cardekho.com/cars/Force",
        "https://www.cardekho.com/cars/Mercedes-Benz",
        "https://www.cardekho.com/cars/Lamborghini",
        "https://www.cardekho.com/cars/Mclaren",
        "https://www.cardekho.com/cars/Maserati",
        "https://www.cardekho.com/cars/PMV",
        "https://www.cardekho.com/cars/Mini",
        "https://www.cardekho.com/porsche-cars",
        "https://www.cardekho.com/cars/Strom_Motors",
        "https://www.cardekho.com/cars/Vayve_Mobility",
        "https://www.cardekho.com/cars/Volvo",
        "https://www.cardekho.com/bmw-cars",
        "https://www.cardekho.com/cars/Bentley",
        "https://www.cardekho.com/cars/Bajaj",
        "https://www.cardekho.com/cars/Audi",
        "https://www.cardekho.com/cars/Aston_Martin",
        "https://www.cardekho.com/cars/Citroen",
        "https://www.cardekho.com/cars/Volkswagen",
        "https://www.cardekho.com/cars/Nissan",
        "https://www.cardekho.com/cars/Jeep",
        "https://www.cardekho.com/cars/Renault",
        "https://www.cardekho.com/cars/Skoda",
        "https://www.cardekho.com/cars/MG",
        "https://www.cardekho.com/cars/Honda",
        "https://www.cardekho.com/cars/Mahindra",
        "https://www.cardekho.com/cars/Hyundai",
        "https://www.cardekho.com/toyota-cars",
        "https://www.cardekho.com/cars/Kia",
        "https://www.cardekho.com/cars/Tata",
        "https://www.cardekho.com/maruti-suzuki-cars"
    ]
    
    car_details = []

    # Comprehensive prompt to guide extraction of all car models
    extraction_prompt = """
    You are an expert automotive data extractor. Your task is to comprehensively extract detailed information about ALL car models from this specific brand/company page on cardekho.com.

    BRAND-SPECIFIC EXTRACTION INSTRUCTIONS:
    1. This is a company/brand specific page (e.g., Tesla, Tata, Maruti, Hyundai, etc.)
    2. Extract ALL car models listed for this specific brand (could be 1 model like Tesla or 10+ models like Maruti)
    3. For EACH individual car model found on the page:
       - Click through or extract from the individual car details
       - Get complete specifications and pricing information
       - Extract all available variants (some cars have XE, XM, XT, XZ variants, others may have different naming)
    4. Focus on 2025 model year cars if specified, otherwise extract available models
    5. Look for detailed specifications sections for each model
    6. Extract exact pricing for each model/variant

    WHAT TO EXTRACT FROM EACH CAR ON THIS BRAND PAGE:
    For every car model visible (like Tesla Model Y, Tata Tiago, etc.):
    - Model name (e.g., "Model Y", "Tiago", "Nexon")
    - All variants of that model (if any)
    - Exact pricing (ex-showroom prices like ₹59.89 - 73.89 Lakh)
    - Engine/Motor specifications:
      * Engine displacement (cc) or Motor power for electric cars
      * Power output (bhp like 295 bhp)
      * Torque (Nm)
      * Range (km for electric cars like 622 km)
    - Fuel/Energy details:
      * Fuel type (Petrol/Diesel/CNG/Electric)
      * Fuel efficiency (kmpl) or Range (km for electric)
    - Vehicle specifications:
      * Body type (Sedan/SUV/Hatchback like Tesla Model Y is an SUV)
      * Seating capacity (like 5 Seats)
      * Transmission type
    - Safety ratings (if available)
    - Key features and highlights

    INDIVIDUAL CAR PROCESSING:
    - Process each car model separately and thoroughly
    - Look for specification tables, price details, feature lists for each model
    - Some brands like Tesla may have only 1 model, others like Maruti may have 10+ models
    - Extract complete information for each model found
    - Look for "View Offers", "View Details", "Specifications" sections for each car

    COVERAGE APPROACH:
    - Start with the main brand page overview
    - Identify all available models for this brand
    - Go through each model individually to extract complete details
    - Handle both simple pages (like Tesla with 1 model) and complex pages (like Maruti with many models)
    - Ensure no model is missed from the brand's lineup

    For the given example: Tesla page should extract complete details for Model Y including its ₹59.89 - 73.89 Lakh price, 622 km range, 295 bhp power, 5-seat capacity, electric fuel type, etc.
    """

    # 3. Define the schema as a Python dictionary, not a prompt string
    extraction_schema = {
        "type": "object",
        "properties": {
            "variants": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "manufacturer": {"type": "string", "description": "Brand name, e.g., Tata"},
                        "model_name": {"type": "string", "description": "Car model, e.g., Tiago"},
                        "manufacturing_year": {"type": "string", "description": "The model year, e.g., 2025"},
                        "variant_name": {"type": "string", "description": "The specific variant name from the table row"},
                        "showroom_price": {"type": "string", "description": "The ex-showroom price for this variant"},
                        "fuel_type": {"type": "string", "description": "e.g., Petrol/Diesel/CNG"},
                        "engine_capacity_cc": {"type": "integer", "description": "Engine displacement in cc"},
                        "body_type": {"type": "string", "description": "Hatchback/Sedan/SUV"},
                        "seating_capacity": {"type": "integer", "description": "Number of seats"},
                        "torque_nm": {"type": "string", "description": "Torque value with units, e.g., 95 Nm"},
                        "mileage_kmpl": {"type": "string", "description": "Fuel efficiency, e.g., 19.01 kmpl"},
                        "power_bhp": {"type": "string", "description": "Power output, e.g., 72.41 bhp"},
                        "transmission": {"type": "string", "description": "Manual or Automatic"},
                        "safety_rating": {"type": "string", "description": "Global NCAP rating, e.g., 4 Star"},
                        "features": {"type": "array", "items": {"type": "string"}, "description": "List of key features"}
                    }
                }
            }
        }
    }

    for url in test_urls:
        print(f"\nScraping: {url}")
        props = await extract_cars(url, extraction_schema, extraction_prompt)
        if props:
            car_details.extend(props)
        
        print("Waiting 10 seconds before next request...")
        await asyncio.sleep(10)
    
    print(f"\n🎉 Total cars extracted: {len(car_details)}")
    
    if car_details:
        # Convert to CSV
        df = convert_to_csv(car_details)
        
        print("\n--- Raw JSON Data (first 2 cars) ---")
        preview_data = [c.__dict__ for c in car_details[:2]]
        print(json.dumps(preview_data, indent=2))
        
        return car_details, df
    else:
        print("❌ No car data extracted")
        return [], None

if __name__ == "__main__":
    asyncio.run(fetch_vehicle_data())