import { Hono } from 'hono'
import prisma from '../client/client'
import { z } from 'zod'


const userRouter = new Hono()

const userSchema = z.object({
    name: z.string().min(1),
    preferredlanguage: z.string().min(1),
    interestScore: z.number().min(1).max(10),
    Sentiment: z.string().min(1),
    phoneNumber: z.string().min(1),
    callduration: z.number().min(1),
    car_details: z.object({
        manufacturer: z.string().min(1).optional(),
        model: z.string().min(1).optional(),
        variant: z.string().min(1).optional(),
        year: z.number().min(1).optional()
    })
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
            callduration: true
        }
    })
    return c.json(users)
})

userRouter.post('/create', async (c) => {
    const body = await c.req.json()
    const parsed = userSchema.safeParse(body)
    if (!parsed.success) {
        return c.json({ error: parsed.error.message }, 400)
    }

    const { name, preferredlanguage, interestScore, Sentiment, phoneNumber, callduration } = parsed.data

    try {
        const user = await prisma.user.create({
            data: { name, preferredlanguage, interestScore, Sentiment, phoneNumber, callduration },
            select: {
                id: true,
                name: true,
                preferredlanguage: true,
                interestScore: true,
                Sentiment: true,
                phoneNumber: true,
                callduration: true
            }
        })
        return c.json(user)
    } catch (error) {
        return c.json({ error: "Failed to create user" }, 500)
    }
})


export default userRouter