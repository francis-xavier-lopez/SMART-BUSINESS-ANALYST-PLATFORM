// Revenue Chart

const chartLabels = JSON.parse(
    document.getElementById("chart-labels").textContent
);

const chartValues = JSON.parse(
    document.getElementById("chart-values").textContent
);

const revenueChartTitle = JSON.parse(
    document.getElementById("revenue-chart-title").textContent
);
console.log(revenueChartTitle);

new Chart(document.getElementById("revenueChart"), {

    type: "line",

    data: {

        labels: chartLabels,

        datasets: [{

            data: chartValues,

            borderColor: "#38C6D9",

            backgroundColor: "rgba(56,198,217,0.15)",

            pointBackgroundColor: "#38C6D9",

            pointRadius: 4,

            pointHoverRadius: 7,

            borderWidth: 3,

            tension: 0.4,

            fill: true

        }]

    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        scales: {

            x: {

                ticks: { color: "#6B6B7D", maxTicksLimit: 7, autoSkip: true },

                grid: { color: "#1E2136", drawBorder: false }

            },

            y: {

                ticks: { color: "#6B6B7D" },

                grid: { color: "#1E2136", drawBorder: false }

            }

        },

        plugins: {

            legend: {

                display: false

            },

            title: {

                display: true,

                text: revenueChartTitle,

                align: "start",

                color: "#D6D5E3",

                padding: { bottom: 16 },

                font: {

                    size: 13,

                    weight: "600"

                }

            }

        }

    }

});

// Product Chart

const productLabels = JSON.parse(
    document.getElementById("product-labels").textContent
);

const productValues = JSON.parse(
    document.getElementById("product-values").textContent
);

const productChartTitle = JSON.parse(
    document.getElementById("product-chart-title").textContent
);

const productColors = [
    "#B23DD1",
    "#A047D6",
    "#8B4FD8",
    "#7657DA",
    "#6A5EDC",
    "#5C6DE0",
    "#4A6BD8",
    "#3E7ADC",
    "#38C6D9"
];

new Chart(document.getElementById("productChart"), {

    type: "bar",

    data: {

        labels: productLabels,

        datasets: [{

            data: productValues,

            backgroundColor: productColors,

            borderWidth: 0,

            borderRadius: 4

        }]

    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        scales: {

            x: {

                ticks: { color: "#6B6B7D" },

                grid: { display: false, drawBorder: false }

            },

            y: {

                ticks: { color: "#6B6B7D" },

                grid: { color: "#1E2136", drawBorder: false }

            }

        },

        plugins: {

            legend: {

                display: false

            },

            title: {

                display: true,

                text: productChartTitle,

                align: "start",

                color: "#D6D5E3",

                padding: { bottom: 16 },

                font: {

                    size: 13,

                    weight: "600"

                }

            }

        }

    }

});


// Category Chart

const categoryLabels = JSON.parse(
    document.getElementById("category-labels").textContent
);

const categoryValues = JSON.parse(
    document.getElementById("category-values").textContent
);

const categoryChartTitle = JSON.parse(
    document.getElementById("category-chart-title").textContent
);

const categoryColors = ["#38C6D9", "#D93D9C", "#E8A33D", "#B23DD1", "#6A5EDC"];

new Chart(document.getElementById("categoryChart"), {

    type: "pie",

    data: {

        labels: categoryLabels,

        datasets: [{

            data: categoryValues,

            backgroundColor: categoryColors,

            borderColor: "#1B1E31",

            borderWidth: 2

        }]

    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        plugins: {

            legend: {

                position: "bottom",

                labels: { color: "#D6D5E3", boxWidth: 10, padding: 16 }

            },

            title: {

                display: true,

                text: categoryChartTitle,

                align: "start",

                color: "#D6D5E3",

                padding: { bottom: 12 },

                font: {

                    size: 13,

                    weight: "600"

                }

            }

        }

    }

});


// Monthly Chart

const monthlyLabels = JSON.parse(
    document.getElementById("monthly-labels").textContent
);

const monthlyValues = JSON.parse(
    document.getElementById("monthly-values").textContent
);

const monthlyChartTitle = JSON.parse(
    document.getElementById("monthly-chart-title").textContent
);

new Chart(document.getElementById("monthlyChart"), {

    type: "line",

    data: {

        labels: monthlyLabels,

        datasets: [{

            data: monthlyValues,

            borderColor: "#B23DD1",

            backgroundColor: "rgba(178,61,209,0.15)",

            pointBackgroundColor: "#B23DD1",

            pointRadius: 4,

            pointHoverRadius: 7,

            borderWidth: 2,

            fill: false,

            tension: 0.3

        }]

    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        scales: {

            x: {

                ticks: { color: "#6B6B7D" },

                grid: { color: "#1E2136", drawBorder: false }

            },

            y: {

                ticks: { color: "#6B6B7D" },

                grid: { color: "#1E2136", drawBorder: false }

            }

        },

        plugins: {

            legend: {

                display: false

            },

            title: {

                display: true,

                text: monthlyChartTitle,

                align: "start",

                color: "#D6D5E3",

                padding: { bottom: 16 },

                font: {

                    size: 13,

                    weight: "600"

                }

            }

        }

    }

});



const logoutBtn = document.getElementById("logoutBtn");

if (logoutBtn) {

    logoutBtn.addEventListener("click", function (e) {

        e.preventDefault();

        Swal.fire({
            title: "Logout?",
            text: "Are you sure you want to logout?",
            icon: "question",
            background: "#1B1E31",
            color: "#ffffff",
            confirmButtonColor: "#B23DD1",
            cancelButtonColor: "#D93D9C",
            confirmButtonText: "Yes, Logout",
            cancelButtonText: "Cancel",
            showCancelButton: true
        }).then((result) => {

            if (result.isConfirmed) {
                window.location.href = logoutUrl;
            }

        });

    });

}