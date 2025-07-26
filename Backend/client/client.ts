import { PrismaClient } from '../src/generated/prisma/edge'
import { withAccelerate } from '@prisma/extension-accelerate'

const prisma = new PrismaClient({
  datasourceUrl: "prisma+postgres://accelerate.prisma-data.net/?api_key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqd3RfaWQiOjEsInNlY3VyZV9rZXkiOiJza19hMkJsamRDcEFPZnNMWGxfUTZ1RDMiLCJhcGlfa2V5IjoiMDFLMTMySEUzNzdBMlJGREg1MFNBS01XSlAiLCJ0ZW5hbnRfaWQiOiJlM2NiMzNjMjJhYTFiMzJhM2UzNGI4OTMxYzMzMTM3ZGRlMDM3MmM3ZDJlMWRjMGU3ZWMyNWUxYTJkNDYwNDcwIiwiaW50ZXJuYWxfc2VjcmV0IjoiMGJhZTc5OWUtYmNiNC00MmI5LTlmMDEtOGViMjE0ZGQ5YjQyIn0.WW9jr685C-jtfCqshj6vO-cT55Y7fFU_d_2XaDXXxmQ",
}).$extends(withAccelerate())
  
  export default prisma;
  