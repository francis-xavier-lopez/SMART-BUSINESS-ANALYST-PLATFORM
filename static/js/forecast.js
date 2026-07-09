const months = JSON.parse(
    document.getElementById("months-data").textContent
);

const revenues = JSON.parse(
    document.getElementById("revenues-data").textContent
);

months.push("Prediction");
revenues.push(prediction);

const ctx = document.getElementById("forecastChart");

new Chart(ctx, {
    type: "line",

    data: {
        labels: months,

        datasets: [{
            label: "Revenue",
            data: revenues,
            borderColor: "#3b82f6",
            backgroundColor: "rgba(59,130,246,0.2)",
            fill: true,
            tension: 0.3,
            pointRadius: 5,
            pointHoverRadius: 8
        }]
    },

    options: {
        responsive: true,

        plugins: {
            legend: {
                display: false
            }
        },

        scales: {
            x: {
                ticks: {
                    color: "white"
                }
            },

            y: {
                ticks: {
                    color: "white"
                }
            }
        }
    }
});