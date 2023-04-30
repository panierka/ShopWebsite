import { useFormik } from "formik";
import * as Yup from "yup";

export function SignUp(){

    const formik = useFormik({
        initialValues: {
            email: "",
            password: "",
            confirmPassword: ""
        },

        validationSchema: Yup.object({
            email: Yup.string().email().required(),
            password: Yup.string().min(6).required(),
            confirmPassword: Yup.string().oneOf([Yup.ref('password')], 'passwords must match').required()
        }),

        onSubmit: (values) => {
            fetch('/add-user', {
                method: 'POST',
                headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    "email": values.email,
                    "password": values.password
                })
              })
        }
    });

    return(
        <>
        <form onSubmit={formik.handleSubmit}>
        <div>
            <label htmlFor="email">Email</label>
            <input
            id="email"
            name="email"
            type="email"
            value={formik.values.email}
            onChange={formik.handleChange}
            />
            {formik.errors.email && formik.touched.email ? (
            <div>{formik.errors.email}</div>
            ) : null}
        </div>
        <div>
            <label htmlFor="password">Password</label>
            <input
            id="password"
            name="password"
            type="password"
            value={formik.values.password}
            onChange={formik.handleChange}
            />
            {formik.errors.password && formik.touched.password ? (
            <div>{formik.errors.password}</div>
            ) : null}
        </div>
        <div>
            <label htmlFor="confirmPassword">Confirm password</label>
            <input
            id="confirmPassword"
            name="confirmPassword"
            type="password"
            value={formik.values.confirmPassword}
            onChange={formik.handleChange}
            />
            {formik.errors.confirmPassword && formik.touched.confirmPassword ? (
            <div>{formik.errors.confirmPassword}</div>
            ) : null}
        </div>
        <button type="submit">Submit</button>
        </form>
        </>
    )
}