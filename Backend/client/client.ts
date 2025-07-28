import { PrismaClient } from '../src/generated/prisma/edge'
import { withAccelerate } from '@prisma/extension-accelerate'

const prisma = new PrismaClient({
  datasourceUrl: "prisma+postgres://accelerate.prisma-data.net/?api_key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqd3RfaWQiOjEsInNlY3VyZV9rZXkiOiJza19zYThkZHJZVEgwREhBc045bk5wTGoiLCJhcGlfa2V5IjoiMDFLMThEOUFXNjY2WFZBMTFUU1NBRTlXSlIiLCJ0ZW5hbnRfaWQiOiIxOGQxZmJlMDA0ZjgzOTZmMzkzYzViODMwYzE3YTBhYzEwYzJlMjE2N2Q4Mjk1NmRjZDU0YmE5NWE5ZGVkZWQzIiwiaW50ZXJuYWxfc2VjcmV0IjoiMzg3OWNiY2YtZDkzNy00MDdhLWIxODAtYzZiZjczYmU4YWE0In0.n6j0DZT41gYVH1hiZpD10jN3bjudFxah2DxBICopruc",
}).$extends(withAccelerate())
  
  export default prisma;
  