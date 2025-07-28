import { Hono } from 'hono'
import userRouter from '../routes/user'
import { cors } from 'hono/cors'

const app = new Hono()

app.use('*', cors())
app.route('/api/user', userRouter)

export default app
