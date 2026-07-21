const months = JSON.parse(
    document.getElementById("months-data").textContent
);

const revenues = JSON.parse(
    document.getElementById("revenues-data").textContent
);

const actualCount = revenues.length;

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
            borderColor: "#38C6D9",
            backgroundColor: "rgba(56,198,217,0.12)",
            fill: true,
            tension: 0.3,
            borderWidth: 2.5,
            pointRadius: (context) => context.dataIndex === actualCount ? 6 : 4,
            pointHoverRadius: 8,
            pointBackgroundColor: (context) => context.dataIndex === actualCount ? "#B23DD1" : "#38C6D9",
            pointBorderColor: "#12152A",
            pointBorderWidth: 2,
            segment: {
                borderColor: (context) => context.p1DataIndex === actualCount ? "#B23DD1" : "#38C6D9",
                borderDash: (context) => context.p1DataIndex === actualCount ? [6, 4] : undefined
            }
        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,

        plugins: {
            legend: {
                display: false
            }
        },

        scales: {
            x: {
                ticks: {
                    color: "#6B6B7D"
                },
                grid: {
                    color: "#1E2136",
                    drawBorder: false
                }
            },

            y: {
                ticks: {
                    color: "#6B6B7D"
                },
                grid: {
                    color: "#1E2136",
                    drawBorder: false
                }
            }
        }
    }
});