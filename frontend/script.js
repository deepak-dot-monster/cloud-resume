fetch("https://6qd7spjxof.execute-api.ap-south-1.amazonaws.com/Prod/count")
  .then(response => response.json())
  .then(data => {
    document.getElementById("visitor-count").textContent = data.count;
  })
  .catch(error => {
    document.getElementById("visitor-count").textContent = "Error loading count";
    console.error(error);
  });