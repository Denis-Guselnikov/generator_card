const searchField = document.querySelector('#searchField');

const appTable = document.querySelector('.app-table');
const tableOutput = document.querySelector('.table-output');
const paginationContainer = document.querySelector(".pagination-container");
const tbody = document.querySelector('.table-body');
const noResults = document.querySelector(".no-results");

tableOutput.style.display = 'none';

searchField.addEventListener("keyup", (e) => {
    const searchValue = e.target.value;
    
    if(searchValue.trim().length > 0) {
        paginationContainer.style.display = 'none';
        tbody.innerHTML = "";
        fetch("/search_card/", {
            body: JSON.stringify({ searchText: searchValue }),
            method: "POST",
        }).then((res) => res.json())
          .then((data) => { 
            console.log("data", data);

            appTable.style.display = 'none';
            tableOutput.style.display = 'block';

            console.log("data.length", data.length);

            if (data.length === 0) {
                noResults.style.display = "block";
                tableOutput.style.display = "none";
            } else {
                noResults.style.display = "none";
                data.forEach((item) => {
                tbody.innerHTML += `
                    <tr>
                    <td>${item.first_name}</td>
                    <td>${item.last_name}</td>
                    <td>${item.card_series}</td>
                    <td>${item.number_card}</td>
                    <td>${item.amount}</td>
                    <td>${item.data_created}</td>
                    <td>${item.data_end}</td>
                    <td>${item.status}</td>
                    </tr>`;
              });
            }           
        });
    } else {
        tableOutput.style.display = 'none';
        appTable.style.display = 'block';
        paginationContainer.style.display = 'block';
    }
});
