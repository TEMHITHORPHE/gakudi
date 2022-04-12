
const copyID = "q165";
const linkDisplayID = "q170"
const storeLinkID = "q168"
const homeIconID = "q176"
copyButton = document.getElementById(copyID);

copyButton.addEventListener("click", function(ev) {
    const link = document.getElementById(linkDisplayID).innerText;
    console.log("COPY!!!!")
    if (navigator.clipboard) {
        navigator.clipboard.writeText(link);
        console.log("Copied!!!");
    }
    else {
        console.log("Not done!!");
    }
})

