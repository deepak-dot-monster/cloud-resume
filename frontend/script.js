fetch("https://6qd7spjxof.execute-api.ap-south-1.amazonaws.com/Prod/count")
  .then(response => response.json())
  .then(data => {
    document.getElementById("visitor-count").textContent = String(data.count).padStart(3, '0');
  })
  .catch(error => {
    document.getElementById("visitor-count").textContent = "ERR";
    console.error(error);
  });