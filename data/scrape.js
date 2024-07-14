const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://transparency.entsoe.eu/transmission/r2/dailyImplicitAllocationsCongestionIncome/show?name=&defaultValue=false&viewType=TABLE&areaType=BORDER_BZN&atch=false&dateTime.dateTime=03.01.2020+00:00|UTC|DAY&border.values=CTY|10YFI-1--------U!BZN_BZN|10YFI-1--------U_BZN_BZN|10Y1001A1001A39I&dv-datatable-detail_5e0c882d3991bd5b98c4dee2_length=100&dv-datatable_length=10', { waitUntil: 'networkidle0' }); // Wait until all network requests have finished

    let data = [];
    let nextPageExists = true;

    while (nextPageExists) {
        const newData = await page.evaluate(() => {
            let table = document.querySelector('table'); // Select the table using the appropriate CSS selector
            if (!table) return null; // Return null if the table doesn't exist
            let rows = Array.from(table.rows);
            return rows.map(row => Array.from(row.cells).map(cell => cell.textContent));
        });

        data = data.concat(newData);

        const nextPageButton = await page.$eval('#dv-datatable-detail_5e0dd9b9623a72234b4343fe_next-custom', elem => elem.click());

        if (nextPageButton !== null) {
            await page.waitForNavigation({ waitUntil: 'networkidle0' }); // Increase timeout to 60 seconds
        } else {
            nextPageExists = false;
        }
    }

    console.log(data); // Logs the table data as a 2D array
    await browser.close();
})();