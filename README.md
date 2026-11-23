# dev-ops-assignment1

## Part 1
1. Run "Hello World" container and observe the results:
   * To run this container we need to execute this command:
   > docker run hello-world
   ![hello-world.png](screenshots/hello-world.png)
   * Docker run will create and run the "hello-world" image container, which will be pulled from docker hub, The output shows us the hello world output and confirms that docker is working properly, we also see the step-by-step explanation of what docker is doing under the hood

2. Run interactive ubuntu container
   * 


ნაწილი 1: კონტეინერების გაშვება და შესწავლა
1. გაუშვით Hello World კონტეინერი და დააკვირდით მიღებულ შედეგს.
2. გაუშვით ინტერაქტიული Ubuntu კონტეინერი.
3. კონტეინერის შიგნით დააინსტალირეთ curl და შეამოწმეთ ინტერნეტთან წვდომა.
4. გამოდით კონტეინერიდან.
5. გამოიტანეთ ყველა კონტეინერის სია, გააჩერეთ და წაშალეთ ერთ-ერთი მათგანი (არასავალდებულო).


ნაწილი 2: საკუთარი Python აპლიკაციის იმიჯის შექმნა (Build)
1. შექმენით სამუშაო საქაღალდე (Folder) თქვენი პროექტისთვის.
2. შექმენით მარტივი Python სკრიპტი.
3. შექმენით Dockerfile.
4. ააწყვეთ (Build) Docker იმიჯი.
5. გაუშვით კონტეინერი შექმნილი იმიჯიდან.
6. მიანიჭეთ იმიჯს თეგი (Tag) და გამოიტანეთ ყველა იმიჯის სია.

ნაწილი 3: Docker Volume-ების გამოყენება მონაცემების შესანახად
1. შექმენით სახელდებული (Named) Docker Volume.
2. გაუშვით კონტეინერი მიბმული (Mounted) Volume-ით.
3. კონტეინერის შიგნით შექმენით და შეინახეთ რაიმე ფაილი.
4. გაუშვით სხვა კონტეინერი იმავე Volume-ის გამოყენებით და დაადასტურეთ, რომ ფაილი შენახულია.