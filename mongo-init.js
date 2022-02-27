// Add things that you want to be executed each time it is instantiated.

print('Start #################################################################');

db.createUser(
    {
        user: process.env.MongoUserName,
        pwd: process.env.MongoPassWord,
        roles: [
            {
                role: "readWrite",
                db: "fast_compiler"
            }
        ]
    }
);

print('END #################################################################');