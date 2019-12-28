function biodata(name, age){
    return JSON.stringify({
         name : name,
         age : age,
         addres : 'Lombok timur NTB',
         hobbies : ['Nontong fllm', 'Belajar', 'Berpikir'],
         is_married : false,
         list_school : [
            {
                name : 'SDN 1 BUNGTIANG',
                year_in : 2001,
                year_out : 2006,
                major : null
            },
            {
                name : 'MTS NW BIRRUL WALIDAIN',
                year_in : 2007,
                year_out : 2010,
                major : null
            },
            {
                name : 'MA NW RENSING RAJAK',
                year_in : 2011,
                year_out : 2013,
                major : null
            }
        ],
         skils : [
            {
                sill_name : 'HTML',
                level : 'expert'

            },
            {
                sill_name : 'Javascript',
                level : 'advance'

            },
            {
                sill_name : 'python',
                level : 'advance'

            }
        ],
         interest_in_coding : true
    }); 

}

let myBio = biodata('Robialta bimara suenri', 23);
console.log(myBio)