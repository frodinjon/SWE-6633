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
    breed:'miniature dachshund',
    cost:10000,
    isAdopted:true,
    imageName:'tempValue'},
    {
    petId:1,
    name:'Jack',
    breed:'miniature dachshund',
    cost:10000,
    isAdopted:true,
    imageName:'tempValue'},
    {
    petId:2,
    name:'Jack',
    breed:'miniature dachshund',
    cost:10000,
    isAdopted:true,
    imageName:'tempValue'},
    {petId:3,
    name:'Jack',
    breed:'miniature dachshund',
    cost:10000,
    isAdopted:true,
    imageName:'tempValue'},
    {
    petId:4,
    name:'Jack',
    breed:'miniature dachshund',
    cost:10000,
    isAdopted:true,
    imageName:'tempValue'},
    {
    petId:5,
    name:'Jack',
    breed:'miniature dachshund',
    cost:10000,
    isAdopted:true,
    imageName:'tempValue'},
    {
    petId:6,
    name:'Jack',
    breed:'miniature dachshund',
    cost:10000,
    isAdopted:true,
    imageName:'tempValue'},
    {
    petId:7,
    name:'Jack',
    breed:'miniature dachshund',
    cost:10000,
    isAdopted:true,
    imageName:'tempValue'}];

  ngOnInit(): void {

    this.getAllPets();
    
  }

  //uncomment once API is working
  getAllPets() {
    // this.service.getAllPets().subscribe((data:Pet[]) => this.pets = data);
    return this.tempPets;
  }

}
