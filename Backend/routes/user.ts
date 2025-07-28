import { Hono } from 'hono'
import prisma from '../client/client'
import { z } from 'zod'


const userRouter = new Hono()

// Schema for car details object
const carDetailsObjectSchema = z.object({
    manufacturer: z.string().min(1),
    model: z.string().min(1),
    variant: z.string().min(1),
    year: z.string().min(1)
})

const userSchema = z.object({
    name: z.string().min(1),
    preferredlanguage: z.string().min(1),
    interestScore: z.number().min(1).max(10),
    Sentiment: z.string().min(1),
    phoneNumber: z.string().min(1),
    callduration: z.number().min(1),
    car_details: z.union([
        z.string().refine((val) => {
            try {
                const parsed = JSON.parse(val)
                return carDetailsObjectSchema.safeParse(parsed).success
            } catch {
                return false
            }
        }, "car_details must be a valid JSON string with manufacturer, model, variant, and year"),
        carDetailsObjectSchema
    ])
})

userRouter.get('/all', async (c) => {
    const users = await prisma.user.findMany({
        select: {
            id: true,
            name: true,
            preferredlanguage: true,
            interestScore: true,
            Sentiment: true,
            phoneNumber: true,
            callduration: true,
            car_details: true
        }
    })
    return c.json(users)
})

userRouter.delete('/delete', async (c) => {
    const response = await prisma.user.deleteMany()
    return c.json(response)
})

userRouter.post('/create', async (c) => {
    const body = await c.req.json()
    const parsed = userSchema.safeParse(body)
    if (!parsed.success) {
        return c.json({ error: parsed.error.message }, 400)
    }

    const { name, preferredlanguage, interestScore, Sentiment, phoneNumber, callduration, car_details } = parsed.data
    
    // Convert car_details to JSON string if it's an object
    const carDetailsString = typeof car_details === 'string' ? car_details : JSON.stringify(car_details)

    try {
        const user = await prisma.user.create({
            data: { 
                name, 
                preferredlanguage, 
                interestScore, 
                Sentiment, 
                phoneNumber, 
                callduration,
                car_details: carDetailsString
            },
            select: {
                id: true,
                name: true,
                preferredlanguage: true,
                interestScore: true,
                Sentiment: true,
                phoneNumber: true,
                callduration: true,
                car_details: true
            }
        })
        return c.json(user)
    } catch (error) {
        return c.json({ error: "Failed to create user" }, 500)
    }
})


export default userRouter