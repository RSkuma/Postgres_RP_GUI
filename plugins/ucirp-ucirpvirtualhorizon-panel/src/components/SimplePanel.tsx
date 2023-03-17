import React from 'react';
import { PanelProps } from '@grafana/data';
import { SimpleOptions } from 'types';
import { css, cx } from '@emotion/css';
import { useStyles2, useTheme2 } from '@grafana/ui';

interface Props extends PanelProps<SimpleOptions> {}

const getStyles = () => {
  return {
    wrapper: css`
      font-family: Open Sans;
      position: relative;
    `,
    svg: css`
      position: absolute;
      top: 0;
      left: 0;
    `,
    textBox: css`
      position: absolute;
      bottom: 0;
      left: 0;
      padding: 10px;
    `,
  };
};

export const SimplePanel: React.FC<Props> = ({ options, data, width, height }) => {
  const theme = useTheme2();
  const styles = useStyles2(getStyles);
  const radius = 100;
  const gap = options.gap;
  // const angles_degrees = [Math.PI/4, 3*Math.PI/4, 5*Math.PI/4, 7*Math.PI/4, 0, Math.PI/2, Math.PI, 3*Math.PI/2]
  let empAngleDegrees = [];
  let angles_degrees = [];
  let j = 0;
  for(let x = 0;x<=360;x = x + gap) {
	if(j % options.gapBetweenEmpMarks === 0) {
		empAngleDegrees.push(x);
	} else {
  		angles_degrees.push(x);
	}
	j++;
  }
  let angles = angles_degrees.map((x) => x/180  * Math.PI);
  let empAngleRadians = empAngleDegrees.map((x) => x/180 * Math.PI);
  const currTilt = data.series
  	.map((x) => x.fields.find((y) => y.type === 'number'))
	.map((t) => t?.values.get(t.values.length - 1))[0];
  const currTiltRadians = currTilt/180 * Math.PI;
  return (
   <div
      className={cx(
        styles.wrapper,
        css`
          width: ${width}px;
          height: ${height}px;
        `
      )}
    >
      <svg
        className={styles.svg}
        width={width}
        height={height}
        xmlns="http://www.w3.org/2000/svg"
        xmlnsXlink="http://www.w3.org/1999/xlink"
        viewBox={`-${width / 2} -${height / 2} ${width} ${height}`}
      >
        <g>
          <circle stroke={theme.colors.background.secondary} style={{ fill: theme.colors.background.secondary }} r={100} strokeWidth="4%"/>
	  {
	  angles.map((i) =>
	  	<line x1={(radius+10)*Math.cos(i)} y1={(radius+10)*Math.sin(i)} x2={(radius-10)*Math.cos(i)} y2={(radius-10)*Math.sin(i)} stroke={theme.colors.secondary.text} strokeWidth="2"/>
	  )
	  }
	  {
	  empAngleRadians.map((i) => 
	  	<line x1={(radius+10)*Math.cos(i)} y1={(radius+10)*Math.sin(i)} x2={(radius-10)*Math.cos(i)} y2={(radius-10)*Math.sin(i)} stroke={theme.colors.secondary.contrastText} strokeWidth="3"/>
	  )	
	  }
  	<line x1={(radius-70)*Math.cos(Math.PI/2 + currTiltRadians)} y1={(radius-70)*Math.sin(Math.PI/2 + currTiltRadians)} x2={(radius-70)*Math.cos(3*Math.PI/2 + currTiltRadians)} y2={(radius-70)*Math.sin(3*Math.PI/2 + currTiltRadians)} stroke={theme.colors.text.primary} strokeWidth="2"/>
  	<line x1={(radius-20)*Math.cos(Math.PI + currTiltRadians)} y1={(radius-20)*Math.sin(Math.PI + currTiltRadians)} x2={(radius-20)*Math.cos(currTiltRadians)} y2={(radius-20)*Math.sin(currTiltRadians)} stroke={theme.colors.text.primary} strokeWidth="2"/>
          <circle stroke={theme.colors.border.strong} style={{ fill: theme.colors.primary.main }} r={7} />
        </g>
      </svg>

      <div className={styles.textBox}>
	<div>Curr Tilt: {currTilt}</div>
      </div>
    </div>
  );
};
