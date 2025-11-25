const app = Vue.createApp({
    data() {
        return {
            intro: 'Welcome to my Vue template',
            show: true,
            petname: "Pet Name",
            species: "Species",
            petlist: [
                {petname: 'Kiki', species: 'Cat'},
                {petname: 'Molly', species: 'Cat'},
                {petname: 'Rover', species: 'Dog'},
                {petname: 'Polly', species: 'Bird'},],
            image: {
                src: './img/catBanner.jpg',
                desc: 'two rows of cat drawings',
            }
        }
    },
    methods: {
        myMethod(){

        },
        AddPet(){
            this.petlist.push({petname: this.petname, species: this.species})
            this.petname = ' '
            this.species = ' '
        },
        Show(){
            this.show = !this.show;
        }
    },
    computed: {
        myComputed() {
            return ''
        },
        
    }
})