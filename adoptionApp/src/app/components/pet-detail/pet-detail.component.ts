import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Pet } from 'src/app/interfaces/pet';
import { ApiService } from 'src/app/services/api.service';
import {MatCardModule} from '@angular/material/card';

@Component({
  selector: 'app-pet-detail',
  templateUrl: './pet-detail.component.html',
  styleUrls: ['./pet-detail.component.css']
})
export class PetDetailComponent implements OnInit{

  constructor(private service:ApiService, private route:ActivatedRoute) {}

  ngOnInit(): void {

    this.route.params.subscribe(params => this.pet = this.tempPets[params['id']])
    
  }

  

  pet:Pet | undefined;

  tempPets:Pet[] = [{
    petId:0,
    name:'Jack',
    breed:'Miniature Dachshund',
    cost:10000,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    isAdopted:true,
    imageName:'assets/dog-1232449_1280.jpg'},
    {
    petId:1,
    name:'Charlie',
    breed:'Quaker Parrot',
    cost:10000,
    isAdopted:true,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    imageName:'assets/images/quaker1.jpg'},
    {
    petId:2,
    name:'Louie',
    breed:'Quaker Parrot',
    cost:10000,
    isAdopted:true,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    imageName:'assets/images/quaker2.jpg'},
    {petId:3,
    name:'Oliver',
    breed:'Cat',
    cost:10000,
    isAdopted:true,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    imageName:'assets/images/cat1.jpg'},
    {
    petId:4,
    name:'Jessie',
    breed:'Dog',
    cost:10000,
    isAdopted:true,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    imageName:'assets/images/dog1.jpg'},
    {
    petId:5,
    name:'Ginger',
    breed:'Dog',
    cost:10000,
    isAdopted:true,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    imageName:'assets/images/dog2.jpg'},
    {
    petId:6,
    name:'Jasmine',
    breed:'Cat',
    cost:10000,
    isAdopted:true,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    imageName:'assets/images/cat2.jpg'},
    {
    petId:7,
    name:'Fruitloop',
    breed:'Dog',
    cost:10000,
    isAdopted:true,
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    imageName:'assets/images/dog3.jpg'}];

  //uncomment once api is running
  getPetById(id:number){
    // this.service.getPetById(id).subscribe((data:Pet) => this.pet = data);
    return this.tempPets[id];
  }
}
