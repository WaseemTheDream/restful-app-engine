(($) ->
    books = [
        {title:"JS the good parts", author:"John Doe", releaseDate:"2012", keywords:"JavaScript"},
        {title:"CS the better parts", author:"John Doe", releaseDate:"2012", keywords:"CoffeeScript"},
        {title:"Scala for the impatient", author:"John Doe", releaseDate:"2012", keywords:"Scala"},
        {title:"American Psyco", author:"Bret Easton Ellis", releaseDate:"2012", keywords:"Novel"},
        {title:"Eloquent JavaScript", author:"John Doe", releaseDate:"2012", keywords:"JavaScript"}
    ]

    Book = Backbone.Model.extend(
        defaults:
            coverImage: "/static/img/placeholder.jpg"
            title: "No title"
            author: "Unknown"
            releaseDate: "Unknown"
            keywords: "None"
        idAttribute:"key"
        )
        # parse: (response) ->
        #     console.log(response)
        #     # response.id = response.key
        #     return response

    BookView = Backbone.View.extend(
        tagName: "div"
        className: "bookContainer"
        template: $("#bookTemplate").html()

        render: ->
            tmpl = _.template(@template)
            @.$el.html(tmpl(@model.toJSON()))
            return @

        events:
            "click .delete": "deleteBook"

        deleteBook: ->
            @model.destroy()
            @.remove()
        )

    Library = Backbone.Collection.extend(
        model: Book
        url: '/api/books'
    )

    LibraryView = Backbone.View.extend(
        el: $("#books")
        initialize: ->
            # @collection = new Library(books)
            @collection = new Library()
            @collection.fetch()
            @render()

            @collection.on("add", @renderBook, @)
            @collection.on("remove", @removeBook, @)
            @collection.on("reset", @render, @)

        render: ->
            that = @
            _.each(@collection.models, ((item) ->
                that.renderBook(item)), @)

        addBook: (e) ->
            e.preventDefault()

            formData = {}
            $("#addBook div").children("input").each((i, el) ->
                if $(el).val() != ""
                    formData[el.id] = $(el).val()
            )
            books.push(formData)
            @collection.create(new Book(formData))

        removeBook: (removedBook) ->
            removedBookData = removedBook.attributes

            _.each(removedBookData, (val, key) -> 
                if (removedBookData[key] == removedBook.defaults[key])
                    delete removedBookData[key]
            )

            _.each(books, (book) ->
                if _.isEqual(book, removedBookData)
                    books.splice(_.indexOf(books, book), 1)
            )

        events:
            "click #add": "addBook"

        renderBook: (item) ->
            bookView = new BookView(
                model: item
            )
            @.$el.append(bookView.render().el)
        )

    libraryView = new LibraryView()

)(jQuery)