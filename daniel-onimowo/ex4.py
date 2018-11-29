# On this day, Nov 29, 2018, scrape the https://punchng.com/ sections as listed below
# 1. JUST IN
# 2. TRENDING
# Return the output as a JSON in Javascript



# 1. JUST IN
justIn = document.querySelectorAll('h3');
let response = {};

for (count = 0; count < justIn.length; count++){
    response[count] = justIn[count].textContent;
}
document.write(JSON.stringify(response))





# 2. TRENDING
trending = document.querySelectorAll('h1');
let response = {};

for (count = 0; count < trending.length; count++){
    response[count] = trending[count].textContent;
}
document.write(JSON.stringify(response))
