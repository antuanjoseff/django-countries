
document.addEventListener("DOMContentLoaded", function(event) { 
    var select_country = document.getElementById('id_country');
    select_country.addEventListener('change', (e)=>{
        ajax(e.target.value)
    })
});

const ajax = (iso3) =>  {
    const url = "http://localhost:8000/countries/get_country_bbox?country=" + iso3
    fetch(url)
        .then(function(response) {
            return response.json();
        })
        .then(function(json) {
            let ext = json[0].bbox
            
            let geojson = json[0].geojson
            
            ext = ext.replaceAll('(', '')
            ext = ext.replaceAll(')', '')
            ext = ext.replaceAll('\'', '')
            ext = ext.replaceAll(', ', ',')

            geodjango_geom.addCountryLayer(geojson)            
        });
}