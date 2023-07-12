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

    this.route.params.subscribe(params => this.getPetById(params['id']))
        
  }

  // pet:Pet | undefined;

  pet:Pet = {
    petId:2,
    name:'Jack',
    breed:'miniature dachshund',
    cost:10000,
    isAdopted:true,
    imageName:'tempValue'}

  //uncomment once api is running
  getPetById(id:number){
    // this.service.getPetById(id).subscribe((data:Pet) => this.pet = data);
    return this.pet;
  }
}
