import React from 'react';
import styled from "styled-components";
import Tabs from "./Tabs";
import CourseCarousel from "./Carousel"; // Import CourseCarousel component
import { useCoursesContext } from '../context/courses_context';

const CourseList = () => {
  const { courses } = useCoursesContext();

  return (
    <CoursesListWrapper>
      <div className='container'>
        <div className='courses-list-top'>
          <h2>A broad selection of courses</h2>
          <p>Choose from 204,000 online video courses with new additions published every month</p>
        </div>

        {/* Replace the previous Tabs with CourseCarousel */}
        <CourseCarousel courses={courses} />
      </div>
    </CoursesListWrapper>
  );
}

const CoursesListWrapper = styled.div`
  padding: 40px 0;
  .courses-list-top p{
    font-size: 1.8rem;
  }
`;

export default CourseList;
