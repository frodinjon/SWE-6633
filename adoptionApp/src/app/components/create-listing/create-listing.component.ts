import { Component, OnInit } from '@angular/core';
import {FormControl, Validators, FormGroup, FormBuilder } from '@angular/forms';
// import { MatSnackBar } from '@angular/material/snack-bar';
// import { Router } from '@angular/router';
// import { AuthenticationService } from 'src/app/services/authentication.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-create-listing',
  templateUrl: './create-listing.component.html',
  styleUrls: ['./create-listing.component.css']
})
export class CreateListingComponent {

  form!: FormGroup;
  petName: string;
  petType: string;
  petAge: number;
  petDescription: string;

  constructor(private http: HttpClient) {}

  submitListing() {
    const petListing = {
      name: this.petName,
      type: this.petType,
      age: this.petAge,
      description: this.petDescription
    };

    // Make an HTTP POST request to the backend API to store the pet listing
    this.http.post('http://your-backend-api-url/create-listing', petListing)
      .subscribe(
        response => {
          // Listing created successfully
          console.log('Listing created:', response);
          this.fetchListings(); // Refresh the listing display
        },
        error => {
          // Error occurred while creating the listing
          console.error('Error creating listing:', error);
        }
      );
  }

  fetchListings() {
    // Make an HTTP GET request to fetch the latest pet listings
    this.http.get('http://your-backend-api-url/listings')
      .subscribe(
        response => {
          // Update the listing display with the fetched listings
          console.log('Fetched listings:', response);
          // TODO: Update your component properties to store and display the fetched listings
        },
        error => {
          // Error occurred while fetching listings
          console.error('Error fetching listings:', error);
        }
      );
  }
}
