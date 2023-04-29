import { useFormik } from "formik";
import * as Yup from "yup";

export function SignUp({text}: {text: string}){

    const formik = useFormik({
        initialValues: {
            name: "",
            email: "",
            password: ""
        },

        validationSchema: {
            name: Yup.string().max(20).required(),
            email: Yup.string().email().required(),
            password: Yup.string().min(6).required()
        },

        onSubmit: (values) => {
            
        }
    })

    return(
        <>
            
        </>
    )
}