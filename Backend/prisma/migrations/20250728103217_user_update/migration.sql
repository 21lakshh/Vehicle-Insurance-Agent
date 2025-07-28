-- CreateTable
CREATE TABLE "User" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "preferredlanguage" TEXT NOT NULL,
    "interestScore" DOUBLE PRECISION NOT NULL,
    "Sentiment" TEXT NOT NULL,
    "phoneNumber" TEXT NOT NULL,
    "callduration" INTEGER NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);
