FROM node:22.13-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all files
COPY . .

# Expose the port
EXPOSE 3000

# Start the service
CMD ["node", "index.mjs"]