// Pegar todos os IDs dentro de uma categoria

function getAllIds() {
    /** @type {number[]} */
    var ids = [];

    document.querySelectorAll(".id a").forEach((el) => {
        const id = el.textContent;
        ids.push(Number(id));
    });

    console.log(ids);
}

getAllIds();
