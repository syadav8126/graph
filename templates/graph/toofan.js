new Chart(document.getElementById("toofanChart"), {
    type: 'line',
    data: {
      //labels: ["Africa", "Asia", "Europe", "Latin America", "North America"],
      labels:[],
      datasets: [
        {
          label: "Population (millions)",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
          data: [{x:10,y:20},{x:20,y:35},{x:20,y:35},{x:20,y:35},{x:20,y:35},{x:20,y:35},{x:20,y:35},{x:20,y:35},{x:20,y:35},]
        }
      ]
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: 'Predicted world population (millions) in 2050'
      }
    }
});