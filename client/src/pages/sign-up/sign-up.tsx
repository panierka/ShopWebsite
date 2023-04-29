import { useFormik } from "formik";
import * as Yup from "yup";

export function SignUp({text}: {text: string}){

    const formik = useFormik({
        initialValues: {
            name: "",
            email: ""
        },

        validationSchema: {
            name: Yup.string().max(20).required(),
            email: Yup.string().email().required()
        },

        onSubmit: (values) => {
            
        }
    })

    return(
        <>
            
        </>
    )
}