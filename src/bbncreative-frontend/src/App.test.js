import React from "react";
import { render } from "@testing-library/react";
import App from "./App";

test("renders placeholder text", () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/placeholder react/i);
  expect(linkElement).toBeInTheDocument();
});
