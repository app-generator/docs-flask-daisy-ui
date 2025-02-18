# Flask + DaisyUI + Vite Starter

A minimal starter template integrating Flask backend with DaisyUI components and Vite frontend tooling.

## Setup

1. Install backend dependencies:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Install frontend dependencies:
```bash
cd frontend
npm install
```

## Development

1. Start the Flask backend:
```bash
cd backend
flask run
```

2. Start the Vite dev server:
```bash
cd frontend
npm run dev
```

3. Visit http://localhost:5173 to see your app

## Production Build

1. Build the frontend:
```bash
cd frontend
npm run build
```

2. The Flask app will serve the built frontend from the dist directory
