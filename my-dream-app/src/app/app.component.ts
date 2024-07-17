import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { HelloWorldComponent} from "./hello-world/hello-world.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule,RouterOutlet,HelloWorldComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent {
  user = ["Jaden", "Sergio", "Fabiana", "Aedo"];
  activated = false; 
}
