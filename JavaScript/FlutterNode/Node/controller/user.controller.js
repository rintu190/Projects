const UserService = require("../service/user.service");

exports.register = async(req,res,next)=>{
    try {
        const {email,password} = req.body;
        const successRes = await UserService.registerUser(email,password);
        res.status(201).json({message: "Successfully Registered", status: 201})
    } catch (error) {
        throw error;
    }
}