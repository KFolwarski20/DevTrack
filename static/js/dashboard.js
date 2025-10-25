document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById('languageChart');
    const labels = JSON.parse(canvas.dataset.labels);
    const data = JSON.parse(canvas.dataset.data);

    const ctx = canvas.getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                label: 'Hours per language',
                data: data,
                backgroundColor: [
                    '#F87171','#60A5FA','#34D399','#FBBF24',
                    '#A78BFA','#F472B6','#FCD34D','#22D3EE'
                ],
                borderColor: '#fff',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 15,
                        font: {
                            size: 14,
                            family: 'Roboto'
                        }
                    }
                }
            },
        }
    });
});
