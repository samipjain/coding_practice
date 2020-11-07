const { GraphQLServer, GraphQLServerLambda } = require('graphql-yoga')

const typeDefs = `
type Query {
    info: String!
}
`

const resolvers = {
    Query: {
        info: () => `This is the API of a hackernews clone`
    }
}

const server = new GraphQLServer({
    typeDefs,
    resolvers,
})
server.start(() => console.log(`Server is running on http://localhost:4000`))