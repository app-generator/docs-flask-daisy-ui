import { defineConfig } from 'vite';
import path from 'path';

export default defineConfig({
    build: {
        outDir: './static/dist',
        emptyOutDir: true,
        rollupOptions: {
            input: {
                main: path.resolve(__dirname, 'static/src/main.js'),
            },
            output: {
                assetFileNames: 'assets/[name].[ext]',
                entryFileNames: 'assets/[name].js',
            },
        },
    },
    server: {
        port: 3000,
    },
});