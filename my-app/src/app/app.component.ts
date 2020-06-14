import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  /**
   * Question1 - For strong highlight to be true, does it mean highlight should also be true?
   * Question2 - Can two objects have same name?
   * Question3 - If we write another query, should it reset the previous highlight or strong highlight?
   * Question4 - 
   * 
   * Approach
   * Step 1 - Design the HTML, write CSS class
   * Step 2 - Render the values using Angular (I should have also mentioned that each object has a highlight and strong property, so write a function to add these 2 new properties in the list)
   * Step 3 - Write JS functions
  */
  title = 'my-app';
  query = '';
  strong_highlight_index = -1;
  highlight_index = []

  list = [
    {
      name: 'angular modules',
      children: [] 
    },
    {
      name: 'angular components',
      children: [] 
    },
    {
      name: 'dependency injection',
      children: [
        {
          name: 'injection in components',
          children: [] 
        },
        {
          name: 'modules and services',
          children: [] 
        },
      ] 
    },
    {
      name: 'angular services for components',
      children: [] 
    },
    {
      name: 'interfaces',
      children: [] 
    },
    {
      name: 'interfaces and components',
      children: [] 
    },
  ]

  ngOnInit() {
    this.resetStyle()
  }

  resetStyle = () => {
    for (let i = 0; i < this.list.length; i++) {
      this.list[i]['highlight'] = false
      this.list[i]['strong_highlight'] = false
      if (this.list[i].children.length > 0) {
        for (let j = 0; j < this.list[i].children.length; j++) {
          this.list[i].children[j]['highlight'] = false
          this.list[i].children[j]['strong_highlight'] = false
        }
      }
    }

    this.highlight_index = []
  }

  submitForm = () => {
    this.resetStyle()
    for (let i = 0; i < this.list.length; i++) {
      let result = []
      let isMatch = false
      if (this.list[i].name.search(this.query) != -1) {
        this.list[i]['highlight'] = true
        result.push(i)
        isMatch = true
      }
      if (this.list[i].children.length > 0) {
        for (let j = 0; j < this.list[i].children.length; j++) {
          if (this.list[i].children[j].name.search(this.query) != -1) {
            this.list[i].children[j]['highlight'] = true
            result.push(i)
            result.push(j)
            isMatch = true
          }
        }
      }
      if (isMatch) {
        this.highlight_index.push(result)
      }
    }
  }

  submitFocus = () => {
    if (this.strong_highlight_index != this.highlight_index.length-1) {
      this.updateCurrentStrongHighlight()
      this.strong_highlight_index++
      let curr_strong = this.highlight_index[this.strong_highlight_index]
      if(curr_strong.length == 1) {
        this.list[curr_strong[0]]['strong_highlight'] = true
      } else {
        this.list[curr_strong[0]].children[curr_strong[1]]['strong_highlight'] = true
      }
    } else {
      this.updateCurrentStrongHighlight()
      this.strong_highlight_index = -1
    }
  }

  updateCurrentStrongHighlight = () => {
    if (this.strong_highlight_index != -1) {
      let curr_index = this.highlight_index[this.strong_highlight_index]
      if(curr_index.length == 1) {
        this.list[curr_index[0]]['strong_highlight'] = false
      } else {
        this.list[curr_index[0]].children[curr_index[1]]['strong_highlight'] = false
      }
    }
  }
}
