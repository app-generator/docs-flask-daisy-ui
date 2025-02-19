import './main.css'; 

document.getElementById('testApi').addEventListener('click', async () => {
    try {
      const response = await fetch('/api/hello')
      const data = await response.json()
      document.getElementById('apiResponse').textContent = data.message
    } catch (error) {
      console.error('Error:', error)
      document.getElementById('apiResponse').textContent = 'Error connecting to API'
    }
  })
  