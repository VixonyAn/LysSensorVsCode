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
                src: './img/SunBtn.png',
                desc: 'Sun Button',
            },
            moonBtn: {
                src: './img/MoonBtn.png',
                desc: 'Moon Button',
            },
            lightSwitch: {
                src: './img/LightOnBtn.png',
                desc: 'Light Switch',
            },
            nightSwitch: {
                src: './img/LightOffBtn.png',
                desc: 'Night Switch',   
            },
            blindsOpen: {
                src: './img/CurtainOpen.png',
                desc: 'Blinds Open',
            },
            blindsClose: {
                src: './img/CurtainClosed.png',
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