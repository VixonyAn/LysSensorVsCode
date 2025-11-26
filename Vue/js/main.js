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
            },

            menuOpen: false,
            uvIndex: 0,
            suncream: 'No suncream needed',
            sunBtn: {
                src: './img/80x80.svg',
                desc: 'Sun Button',
            },
            moonBtn: {
                src: './img/80x80.svg',
                desc: 'Moon Button',
            },
            lightSwitch: {
                src: './img/80x80.svg',
                desc: 'Light Switch',
            },
            nightSwitch: {
                src: './img/80x80.svg',
                desc: 'Night Switch',   
            },
            blindsOpen: {
                src: './img/80x80.svg',
                desc: 'Blinds Open',
            },
            blindsClose: {
                src: './img/80x80.svg',
                desc: 'Blinds Close',
            },
            savedEnergy: 5,

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
        },

        toggleMenu(){
            this.menuOpen = !this.menuOpen;
        }
    },
    computed: {
        myComputed() {
            return ''
        },
        
    }
})