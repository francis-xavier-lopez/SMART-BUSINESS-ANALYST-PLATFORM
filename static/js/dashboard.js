// Revenue Chart

const chartLabels = JSON.parse(
    document.getElementById("chart-labels").textContent
);

const chartValues = JSON.parse(
    document.getElementById("chart-values").textContent
);

new Chart(document.getElementById("revenueChart"), {

    type: "line",

    data: {

        labels: chartLabels,

        datasets: [{

            data: chartValues,

            borderWidth: 3,

            tension: 0.4,

            fill: false

        }]

    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        plugins: {

            legend: {

                display: false

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

new Chart(document.getElementById("productChart"), {

    type: "bar",

    data: {

        labels: productLabels,

        datasets: [{

            data: productValues,

            borderWidth: 1

        }]

    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        plugins: {

            legend: {

                display: false

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

new Chart(document.getElementById("categoryChart"), {

    type: "pie",

    data: {

        labels: categoryLabels,

        datasets: [{

            data: categoryValues

        }]

    },

    options: {

        responsive: true,

        maintainAspectRatio: false

    }

});


// Monthly Chart

const monthlyLabels = JSON.parse(
    document.getElementById("monthly-labels").textContent
);

const monthlyValues = JSON.parse(
    document.getElementById("monthly-values").textContent
);

new Chart(document.getElementById("monthlyChart"), {

    type: "line",

    data: {

        labels: monthlyLabels,

        datasets: [{

            data: monthlyValues,

            borderWidth: 2,

            fill: false,

            tension: 0.3

        }]

    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        plugins: {

            legend: {

                display: false

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
            background: "#1e293b",
            color: "#ffffff",
            confirmButtonColor: "#2563eb",
            cancelButtonColor: "#ef4444",
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