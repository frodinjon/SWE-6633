import { Component, OnInit } from '@angular/core';
import { Pet } from 'src/app/interfaces/pet';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-list-pets',
  templateUrl: './list-pets.component.html',
  styleUrls: ['./list-pets.component.css']
})
export class ListPetsComponent implements OnInit {

  constructor(private service:ApiService){

  }

  pets:Pet[] = [];

  tempPets:Pet[] = [{
    petId:0,
    name:'Jack',
    breed:'Miniature Dachshund',
    cost:10000,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Et netus et malesuada fames ac. Dictum at tempor commodo ullamcorper a lacus vestibulum.",
    isAdopted:true,
    imageName:'assets/dog-1232449_1280.jpg'},
    {
    petId:1,
    name:'Charlie',
    breed:'Quaker Parrot',
    cost:10000,
    isAdopted:true,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Et netus et malesuada fames ac. Dictum at tempor commodo ullamcorper a lacus vestibulum.",
    imageName:'assets/images/quaker1.jpg'},
    {
    petId:2,
    name:'Louie',
    breed:'Quaker Parrot',
    cost:10000,
    isAdopted:true,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Et netus et malesuada fames ac. Dictum at tempor commodo ullamcorper a lacus vestibulum.",
    imageName:'assets/images/quaker2.jpg'},
    {petId:3,
    name:'Oliver',
    breed:'Cat',
    cost:10000,
    isAdopted:true,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Et netus et malesuada fames ac. Dictum at tempor commodo ullamcorper a lacus vestibulum.",
    imageName:'assets/images/cat1.jpg'},
    {
    petId:4,
    name:'Jessie',
    breed:'Dog',
    cost:10000,
    isAdopted:true,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Et netus et malesuada fames ac. Dictum at tempor commodo ullamcorper a lacus vestibulum.",
    imageName:'assets/images/dog1.jpg'},
    {
    petId:5,
    name:'Ginger',
    breed:'Dog',
    cost:10000,
    isAdopted:true,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Et netus et malesuada fames ac. Dictum at tempor commodo ullamcorper a lacus vestibulum.",
    imageName:'assets/images/dog2.jpg'},
    {
    petId:6,
    name:'Jasmine',
    breed:'Cat',
    cost:10000,
    isAdopted:true,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Et netus et malesuada fames ac. Dictum at tempor commodo ullamcorper a lacus vestibulum.",
    imageName:'assets/images/cat2.jpg'},
    {
    petId:7,
    name:'Fruitloop',
    breed:'Dog',
    cost:10000,
    isAdopted:true,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Et netus et malesuada fames ac. Dictum at tempor commodo ullamcorper a lacus vestibulum.",
    imageName:'assets/images/dog3.jpg'}];

  ngOnInit(): void {

    this.getAllPets();
    
  }

  //uncomment once API is working
  getAllPets() {
    // this.service.getAllPets().subscribe((data:Pet[]) => this.pets = data);
    return this.tempPets;
  }

}
