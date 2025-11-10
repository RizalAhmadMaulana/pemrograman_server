# 1. Tentukan base image (Node.js versi LTS)
FROM node:18-alpine

# 2. Tentukan direktori kerja di dalam container
WORKDIR /usr/src/app

# 3. Salin file package.json dan package-lock.json (jika ada)
# Ini dilakukan terpisah agar Docker dapat memanfaatkan cache layer untuk instalasi npm
COPY package*.json ./

# 4. Instal dependencies (Express.js)
RUN npm install

# 5. Salin semua file proyek ke direktori kerja
COPY . .

# 6. Port yang digunakan oleh aplikasi di dalam container
EXPOSE 3000

# 7. Perintah yang dijalankan ketika container dimulai
CMD [ "npm", "start" ]