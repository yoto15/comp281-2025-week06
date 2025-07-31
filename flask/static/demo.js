
document.addEventListener('DOMContentLoaded', main);

function main() {
	const name = document.getElementById('name');
	const message = document.getElementById('message');
	const send = document.getElementById('send');
	const reload = document.getElementById('reload');
	const logs = document.getElementById('logs');

	send.addEventListener('click', () => {
		const data = {
			name: name.value,
			message: message.value
		};

		fetch('/send', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(data)
		})
		.then(response => response.json())
		.then(data => {
			show_logs(data.logs);
		})
		.catch((error) => {
			console.error('Error:', error);
			logs.innerHTML += `<p>Error: ${error.message}</p>`;
		});
	});

	reload.addEventListener('click', () => {
		fetch('/logs')
			.then(response => response.json())
			.then(data => {
				show_logs(data.logs);
			})
			.catch((error) => {
				console.error('Error:', error);
				logs.innerHTML += `<p>Error: ${error.message}</p>`;
			});
	});

	function show_logs(logsData) {
		logs.innerHTML = ''; // Clear previous logs
		logsData.reverse(); // Reverse the order to show the latest logs first
		logsData.forEach(log => {
			const logItem = document.createElement('p');
			logItem.textContent = `
				${log.timestamp} - ${log.name}: ${log.message}
			`;
			logs.appendChild(logItem);
		});
	}
}