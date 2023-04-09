document.querySelectorAll('.read-btn').forEach(btn => {
    btn.addEventListener('click', event => {
      const bookId = event.target.dataset.bookId;

      // event.target.style.backgroundColor = '#FF0066';
      event.target.textContent = 'Already Read';
      fetch('/dashboard', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'  
        },
        body: JSON.stringify({ book_id: bookId })  
      }).then(response => {
        console.log("success")
        return response.json()  
      }).then(data => {
        const readText = document.querySelector(`#${data.book_id}`);
        if (data.is_read) {
          readText.textContent = 'Already read';
        } else {
          readText.textContent = '';
        }
      });
    });
  });
  