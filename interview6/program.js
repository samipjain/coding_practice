/* 

Example display:

Tent & General Rentals
|
-  Joe's Tents, joe@tents.com
|  Services: Tent Rental, Chair Rental, Flooring Rental, Table Rental
|
-  All Photography, photos@allyouneed.com
|  Services: Photo Booth

Food & Beverage
|
-  Super Catering, caterit@food.net
|  Services: Catering

Photography & Video Services
|
-  All Photography, photos@allyouneed.com
|  Services: Photography, Videography

[
    {
      id: "1",
      name: "Tent & General Rentals",
      vendors: [
        {
          id: 1,
          companyName: "Joe's Tents",
          companyEmail:"joe@tents.com",
          services: [
            {
              id: 1,
              name: "",
            },
            {
            },
            
          ]
        },
        {
        }
      ]'
    },
    {
    },
    {
    }
]

*/
output = []

function displayVendors(data) {
  const services = data['serviceCategories']
  const vendors = data['vendors']
  
  services.forEach((service) => {
    let vendor_service_category = {}
    
    
    vendor_service_category['id'] = service['id']
    vendor_service_category['name'] = service['name']
    vendor_service_category['vendors'] = []
    // [28,47,16,15,14,46,40,24,8,7,6,35,3,32]
    
    for (let i = 0; i < vendors.length; i++) {
      vendor_services = vendors[i].services
      let temp_s = []
      vendor_services.forEach((s) => {
          if (data['serviceIDs'].includes(s['id']) {
            temp_s.push({id: s['id'], name: s['name']})
          }
      })
      if (temp_s.length != 0) {
        vendor_service_category['vendors'].push({ id: vendors[i].id, companyName: vendors[i].companyName, companyEmail: vendors[i].companyEmail, services: temp_s})
      }a
    }
  output.push(vendor_service_category)
  })
  
}



const data = 
{
   "vendors":[
      {
         "id":1,
         "companyName":"Joe's Tents",
         "companyEmail":"joe@tents.com",
         "services":[
            {
               "id":3,
               "name":"Tent Rental"
            },
            {
               "id":6,
               "name":"Flooring Rental"
            },
            {
               "id":7,
               "name":"Tables Rental"
            },
            {
               "id":8,
               "name":"Chair Rental"
            }
         ]
      },
      {
         "id":2,
         "companyName":"All Photography",
         "comanyEmail":"photos@allyouneed.com",
         "services":[
            {
               "id":35,
               "name":"Photo Booth"
            },
            {
               "id":1,
               "name":"Photography"
            },
            {
               "id":19,
               "name":"Videography"
            }
         ]
      },
      {
         "id":3,
         "companyName":"Super Catering",
         "companyEmail":"caterit@food.net",
         "services":[
            {
               "id":4,
               "name":"Catering"
            }
         ]
      }
   ],
   "serviceCategories":[
      {
         "id":1,
         "name":"Tent & General Rentals",
         "serviceIDs":[28,47,16,15,14,46,40,24,8,7,6,35,3,32],
          // vendorIDs: [1,2,3,4]
      },
      {
         "id":9,
         "name":"Food & Beverage",
         "serviceIDs": [31,4,18,45,22,42,41,39]
      },
      {
        "id":10,
        "name": "Photography & Video Services",
        "serviceIDs": [19,1]
      }
   ]
}