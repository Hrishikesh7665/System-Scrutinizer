// JS file for System-Scrutinizer 
// Author : Hrishikesh7665 (Hrishikesh Patra) & ninja-hattori (Shabdik Chakraborty)

function createHelpWindow(event) {
    event.preventDefault(); // Prevents default link behavior
    const helpURL = event.currentTarget.href; // Gets the href from the clicked link
    const windowName = "HelpWindow";
    const windowFeatures = "titlebar=1,scrollbars=1,resizable=1,toolbar=1,width=900,height=600";

    if (typeof helpWindow === 'undefined' || helpWindow.closed) {
        helpWindow = window.open(helpURL, windowName, windowFeatures);
    } else {
        helpWindow.location = helpURL;
    }
    helpWindow.focus();
}

function scrollToScoring() {
    document.location.hash = "#top";
    document.location.hash = "#scoringSection";
    document.getElementById("pageBody").scrollTop = 0;
}

function toggleTableBody(event) {
    let tableRow = event;

    // Traverse to find the parent TABLE element
    while (tableRow.tagName !== "TABLE") {
        tableRow = tableRow.parentElement;
    }

    const tbody = tableRow.querySelector("tbody");
    if (tbody.style.display === "none") {
        tbody.style.display = "table-row-group";
        event.innerHTML = event.innerHTML.replace("plus", "minus");
        event.title = "Collapse";
    } else {
        tbody.style.display = "none";
        event.innerHTML = event.innerHTML.replace("minus", "plus");
        event.title = "Expand";
    }
}

function toggleAllTableBodies(event) {
    const shouldExpand = event.title === "Expand";

    if (shouldExpand) {
        event.innerHTML = event.innerHTML.replace("plus", "minus");
        event.title = "Collapse";
        event.nextSibling.nodeValue = event.nextSibling.nodeValue.replace("Expand", "Collapse");
    } else {
        event.innerHTML = event.innerHTML.replace("minus", "plus");
        event.title = "Expand";
        event.nextSibling.nodeValue = event.nextSibling.nodeValue.replace("Collapse", "Expand");
    }

    const reportSections = document.getElementById("Report").children;
    for (let i = 0; i < reportSections.length; i++) {
        if (reportSections[i].className === "ReportSection") {
            const tbody = reportSections[i].querySelector("tbody");
            tbody.style.display = shouldExpand ? "table-row-group" : "none";
            const toggleButton = reportSections[i].querySelector("thead button");
            if (shouldExpand) {
                toggleButton.innerHTML = toggleButton.innerHTML.replace("plus", "minus");
                toggleButton.title = "Collapse";
            } else {
                toggleButton.innerHTML = toggleButton.innerHTML.replace("minus", "plus");
                toggleButton.title = "Expand";
            }
        }
    }
}

// Wait for the document to fully load
document.addEventListener("DOMContentLoaded", function () {
    // Get the button
    const scrollToTopBtn = document.getElementById("scrollToTopBtn");

    // Show the button when scrolling down
    window.onscroll = function () { toggleButtonVisibility() };

    function toggleButtonVisibility() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            scrollToTopBtn.style.display = "block";
        } else {
            scrollToTopBtn.style.display = "none";
        }
    }

    // Scroll to the top of the document
    function scrollToTop() {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For other browsers
    }

    // Attach the scrollToTop function to the button's click event
    scrollToTopBtn.addEventListener("click", scrollToTop);
});