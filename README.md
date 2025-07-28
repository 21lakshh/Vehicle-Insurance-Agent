# 🚗 Vehicle Insurance Call AI Agent

A sophisticated bilingual (Hindi/English) AI voice agent built with **LiveKit** that handles vehicle insurance inquiries, extracts customer information, and stores it in a PostgreSQL database. The agent uses a **Neo4j Graph RAG** system to retrieve relevant car information scraped from **CarDekho.com** using **Firecrawl API**.

![Graph Visualization 1](./public/graph1.png)
![Graph Visualization 2](./public/graph2.png)

## 🌟 Features

### 🎯 Core Capabilities
- **Bilingual Voice Interaction**: Seamless switching between Hindi and English
- **Real-time Voice Conversations**: Using LiveKit's advanced voice pipeline
- **Lead Qualification**: Intelligent conversation flow to assess customer interest
- **Appointment Booking**: Automated scheduling for qualified leads
- **Data Extraction**: Captures customer details, preferences, and vehicle information

### 🚀 Technical Features
- **Graph RAG System**: Neo4j-powered knowledge graph for intelligent car information retrieval
- **Web Scraping**: 200+ car models scraped from CarDekho.com using Firecrawl API
- **Real-time Database**: PostgreSQL with Prisma ORM for data persistence
- **Cloud Infrastructure**: Cloudflare Workers backend deployment
- **Advanced Voice Processing**: Noise cancellation, VAD, and multilingual support

## 🏗️ Architecture

```mermaid
graph TB
    A[LiveKit Voice Interface] --> B[AI Agent - Priya]
    B --> C[Sarvam STT/TTS]
    B --> D[Google Gemini LLM]
    B --> E[Neo4j Graph Database]
    B --> F[PostgreSQL Database]
    
    G[Firecrawl API] --> H[Car Data Scraper]
    H --> I[CSV Data Files]
    I --> E
    
    E --> J[Graph RAG Retrieval]
    J --> B
    
    F --> K[Cloudflare Workers API]
    K --> L[Prisma ORM]
    
    subgraph "Data Sources"
        M[CarDekho.com]
        M --> G
    end
    
    subgraph "Voice Stack"
        N[Silero VAD]
        O[Noise Cancellation]
        P[Turn Detection]
    end
    
    N --> A
    O --> A
    P --> A
```

## 📊 Data Pipeline

### 1. **Car Data Collection**
- **Source**: CarDekho.com (40+ manufacturers)
- **Tool**: Firecrawl API for structured extraction
- **Coverage**: 200+ models with complete specifications
- **Output**: CSV files with detailed car information

### 2. **Graph Database Construction**
- **Database**: Neo4j Graph Database
- **Structure**: Vehicle nodes connected to Manufacturer, BodyType, FuelType, and Feature nodes
- **Relationships**: MANUFACTURED_BY, HAS_BODY_TYPE, USES_FUEL, HAS_FEATURE
- **Purpose**: Enables intelligent retrieval of car information during conversations

### 3. **Voice Conversation Pipeline**
```
User Voice → STT (Sarvam Saarika v2.5) → LLM (Gemini 2.5 Flash) → Graph RAG → TTS (Sarvam Anushka) → User
                                                    ↓
                                            PostgreSQL Storage
```

## 🤖 AI Models & Configuration

### **Voice Processing Models**
- **STT Model**: Sarvam Saarika v2.5 (Hindi/English bilingual)
- **TTS Model**: Sarvam Anushka voice (Hindi/English bilingual)
- **Language Model**: Google Gemini 2.5 Flash
- **Voice Activity Detection**: Silero VAD
- **Turn Detection**: Multilingual model for seamless conversation flow

### **Model Configuration**
```python
stt=sarvam.STT(
    language="hi-IN",
    model="saarika:v2.5",
),
llm=google.LLM(model="gemini-2.5-flash"),
tts=sarvam.TTS(
    target_language_code="hi-IN",
    speaker="anushka",
),
```

## 🛠️ Tech Stack

### **AI & Voice Processing**
- **LiveKit Agents**: Voice conversation framework
- **Sarvam STT**: Speech-to-Text using Saarika v2.5 model (Hindi/English)
- **Sarvam TTS**: Text-to-Speech using Anushka voice (Hindi/English)
- **Google Gemini 2.5 Flash**: Large Language Model for conversation generation
- **Silero VAD**: Voice Activity Detection
- **Multilingual Turn Detection**: Conversation flow management

### **Backend Infrastructure**
- **Cloudflare Workers**: Serverless backend deployment
- **Hono.js**: Fast web framework
- **Prisma ORM**: Database management
- **PostgreSQL**: Primary database
- **TypeScript**: Type-safe development

### **Data & AI**
- **Neo4j**: Graph database for RAG system
- **Firecrawl API**: Web scraping for car data
- **Pandas**: Data processing and analysis
- **LangChain**: Graph database integration

### **Development Tools**
- **Python**: Agent and scraping scripts
- **Node.js**: Backend services
- **Jupyter Notebooks**: Data analysis and graph setup

## 📁 Project Structure

```
Vehicle-Insurance-Agent/
├── agent.py                    # Main LiveKit agent
├── scrapper.py                 # Car data scraper
├── models.py                   # Pydantic data models
├── requirements.txt            # Python dependencies
├── env.local.example          # Environment variables template
│
├── Backend/                    # Cloudflare Workers API
│   ├── src/index.ts           # API entry point
│   ├── routes/user.ts         # User management endpoints
│   ├── prisma/
│   │   ├── schema.prisma      # Database schema
│   │   └── migrations/        # Database migrations
│   ├── package.json           # Node.js dependencies
│   └── tsconfig.json          # TypeScript configuration
│
├── data/                      # Scraped car datasets
│   ├── car_dataset_combined.csv    # Main dataset (200+ models)
│   └── car_data_*.csv              # Individual scraping runs
│
├── notebooks/                 # Data analysis and setup
│   ├── data.ipynb            # Data processing notebook
│   └── graphdb.ipynb         # Neo4j graph setup
│
└── public/                   # Graph visualizations
    ├── graph1.png           # Neo4j graph structure
    └── graph2.png           # Vehicle relationships
```

## 🚀 Setup Instructions

### 1. **Clone Repository**
```bash
git clone <repository-url>
cd Vehicle-Insurance-Agent
```

### 2. **Environment Setup**
```bash
# Copy environment template
cp env.local.example .env.local

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies
cd Backend
npm install
```

### 3. **Configure Environment Variables**
Edit `.env.local` with your API keys:

```env
# Google API Configuration
GOOGLE_API_KEY=your_google_api_key_here

# LiveKit Configuration
LIVEKIT_URL=wss://your-livekit-instance.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

# Sarvam API Configuration
SAKVAM_API_KEY=sk_your_sarvam_api_key

# FireCrawl API Configuration
FIRECRAWL_API_KEY=fc-your_firecrawl_api_key

# Neo4j Configuration
NEO4J_URI=neo4j+s://your-instance.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_neo4j_password

# Groq API Configuration (optional)
GROQ_API_KEY=gsk_your_groq_api_key
```

### 4. **Database Setup**

#### PostgreSQL (Prisma)
```bash
cd Backend
npx prisma generate
npx prisma db push
```

#### Neo4j Graph Database
```bash
# Run the graph setup notebook
jupyter notebook notebooks/graphdb.ipynb
```

### 5. **Data Collection (Optional)**
```bash
# Scrape fresh car data from CarDekho.com
python scrapper.py
```

### 6. **Run Services**

#### Start Backend API
```bash
cd Backend
npm run dev
```

#### Start AI Agent
```bash
python agent.py
```

## 📊 Database Schema

### **PostgreSQL Schema (User Data)**
```sql
model User {
  id                String   @id @default(uuid())
  name              String   @default("")
  preferredlanguage String   @default("")
  interestScore     Float    @default(0)
  Sentiment         String   @default("")
  phoneNumber       String   @default("")
  callduration      Int      @default(0)
  createdAt         DateTime @default(now())
  car_details       Json     @default("{}")
}
```

### **Neo4j Graph Schema**
```cypher
// Nodes
(:Vehicle {manufacturer, model_name, variant_name, ...})
(:Manufacturer {name})
(:BodyType {name})
(:FuelType {name})
(:Feature {name})

// Relationships
(Vehicle)-[:MANUFACTURED_BY]->(Manufacturer)
(Vehicle)-[:HAS_BODY_TYPE]->(BodyType)
(Vehicle)-[:USES_FUEL]->(FuelType)
(Vehicle)-[:HAS_FEATURE]->(Feature)
```

## 🎯 Agent Conversation Flow

### **1. Language Selection**
```
Hindi: "नमस्ते! मैं प्रिया बोल रही हूँ SecureWheels Insurance से। 
       आप हिंदी में बात करना चाहेंगे या English में?"

English: "Hello! This is Priya from SecureWheels Insurance. 
         Would you prefer Hindi or English?"
```

### **2. Information Gathering**
- Customer name and contact details
- Vehicle ownership information
- Specific car model details
- Current insurance status

### **3. Intelligent Car Information Retrieval**
The agent uses the Neo4j Graph RAG to:
- Identify user's car from conversation
- Retrieve relevant specifications
- Provide personalized insurance recommendations
- Answer technical questions about their vehicle

### **4. Lead Qualification & Booking**
- Assess customer interest (1-10 score)
- Analyze sentiment (Positive/Neutral/Negative)
- Book appointments for qualified leads
- Store complete interaction data

## 📈 Dataset Statistics

- **Manufacturers**: 40+ brands (Tesla, Tata, Maruti, Hyundai, BMW, etc.)
- **Total Models**: 200+ different car models
- **Data Points**: 15+ attributes per vehicle
- **Coverage**: Complete specifications, pricing, features
- **Source**: CarDekho.com (real-time market data)

## 🔧 API Endpoints

### **User Management**
```typescript
GET  /api/user/all        # Get all users
POST /api/user/create     # Create new user record
```

### **Request/Response Format**
```json
{
  "name": "John Doe",
  "preferredlanguage": "English",
  "interestScore": 8,
  "Sentiment": "Positive",
  "phoneNumber": "+91-9876543210",
  "callduration": 420,
  "car_details": {
    "manufacturer": "Tata",
    "model": "Nexon",
    "variant": "XZ Plus",
    "year": 2025
  }
}
```

## 🎨 Graph Visualizations

The project includes Neo4j graph visualizations showing:

1. **Graph Structure** (`graph1.png`): Overall node relationships and data model
2. **Vehicle Connections** (`graph2.png`): How vehicles connect to features, manufacturers, and specifications

## 🚀 Deployment

### **Backend (Cloudflare Workers)**
```bash
cd Backend
npm run deploy
```

### **Agent (Local/Server)**
```bash
python agent.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🆘 Support

For questions or issues:
1. Check the documentation above
2. Review the code comments
3. Open an issue in the repository
4. Contact the development team

---

Built with ❤️ using LiveKit, Neo4j, and modern AI technologies 