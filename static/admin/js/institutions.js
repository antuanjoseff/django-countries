
document.addEventListener("DOMContentLoaded", function(event) { 
    
    var select_country = document.getElementById('id_country');
    if (!select_country) return;
    
    // Global variable for this file
    var iso3 = select_country.value

    select_country.addEventListener('change', (e)=>{
        iso3 = e.target.value;
    })
    
    // Check tabs-2 visibility (where map is) and update map (load country or reset map view)
    respondToVisibility(document.getElementById("tabs-2"), visible => {
        if (visible) {
            if (iso3) {
                ajax(iso3)
            } else {
                geodjango_geom.resetMap()
            }
        }
    });    
});

// Load country data and put it in map layer
const ajax = (iso3) =>  {
    
    if (!iso3) {
        return
    }
    const url = "http://localhost:8000/mobility/get_country_bbox?country=" + iso3
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


respondToVisibility = function(element, callback) {
    var options = {
      root: document.documentElement
    }
  
    var observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        callback(entry.intersectionRatio > 0);
      });
    }, options);
  
    observer.observe(element);
  }